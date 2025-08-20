# front_app.py
# Front-end KivyMD moderne (clair/sombre, animations) qui appelle le backend tel_org
# Dépendances : kivy, kivymd, yt-dlp, mutagen (et ffmpeg installé sur le système)
# Exécution PC : python front_app.py
# Pour Android : utiliser buildozer (spec à configurer), ce fichier reste le front et importe tel_org (backend)

import threading
from functools import partial

from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.progressbar import MDProgressBar

# --- Backend ---
# Assurez-vous que tel_org.py (fourni par toi) est dans le même dossier ou sur PYTHONPATH
import tel_org  # expose telecharger_playlist(url) et organiser_musiques()

KV = """
#:import dp kivy.metrics.dp

<CarteGlass@MDCard>:
    radius: [24,]
    elevation: 4
    md_bg_color: app.get_bg_carte()
    padding: dp(20)

<EcranPrincipal>:
    name: "principal"

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(10)

        MDTopAppBar:
            id: barre_app
            title: "RG Musique 🎵"
            elevation: 2
            right_action_items: [["theme-light-dark", lambda x: app.changer_theme()], ["cog", lambda x: app.ouvrir_a_propos()]]

        MDBoxLayout:
            orientation: "vertical"
            padding: dp(16)
            spacing: dp(16)

            CarteGlass:
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(12)

                    MDLabel:
                        id: titre_label
                        text: "Télécharge et organise ta playlist"
                        halign: "center"
                        font_style: "H5"

                    MDTextField:
                        id: url_playlist
                        hint_text: "Colle l'URL de ta playlist YouTube"
                        helper_text: "Ex: https://www.youtube.com/playlist?list=..."
                        helper_text_mode: "on_focus"
                        icon_right: "youtube"
                        size_hint_x: 1

                    MDBoxLayout:
                        spacing: dp(10)
                        adaptive_height: True

                        MDFillRoundFlatIconButton:
                            id: btn_dl
                            icon: "download"
                            text: "Télécharger & organiser"
                            on_release: app.cliquer_telecharger()

                        MDIconButton:
                            id: btn_effacer
                            icon: "broom"
                            tooltip_text: "Effacer l'URL"
                            on_release: url_playlist.text = ""

            CarteGlass:
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(8)

                    MDBoxLayout:
                        adaptive_height: True
                        spacing: dp(8)
                        MDLabel:
                            text: "Progression"
                            bold: True
                        MDLabel:
                            id: pourcent_label
                            text: "0%"
                            halign: "right"

                    MDProgressBar:
                        id: barre_progression
                        value: 0
                        max: 100
                        height: dp(8)

                    MDBoxLayout:
                        adaptive_height: True
                        spacing: dp(8)
                        MDIconButton:
                            id: icone_spinner
                            icon: "motion-play"
                            disabled: True
                        MDLabel:
                            id: statut_label
                            text: "En attente…"
                            theme_text_color: "Secondary"

            CarteGlass:
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(8)

                    MDLabel:
                        text: "Console"
                        bold: True

                    ScrollView:
                        bar_width: dp(6)
                        MDLabel:
                            id: console_label
                            text: "— Prêt —"
                            size_hint_y: None
                            height: self.texture_size[1] + dp(20)
                            text_size: self.width, None
                            halign: "left"

<NavigationPrincipal>:
    transition: SlideTransition()
    EcranPrincipal:
"""


class EcranPrincipal(Screen):
    pass


class NavigationPrincipal(ScreenManager):
    pass


class RGMusiqueApp(MDApp):
    dialog: MDDialog | None = None
    _travail: threading.Thread | None = None
    _telechargement_en_cours: bool = False

    def build(self):
        self.title = "RG Musique"
        self.theme_cls.theme_style = "Dark"  # par défaut nuit
        self.theme_cls.primary_palette = "Indigo"
        root = Builder.load_string(KV)
        Clock.schedule_once(self._animer_titre, 0.2)
        return root

    # --- Helpers UI ---
    def get_bg_carte(self):
        if self.theme_cls.theme_style == "Dark":
            return (1, 1, 1, 0.05)
        return (0, 0, 0, 0.03)

    def _animer_titre(self, *_):
        ecran = self.root.get_screen("principal")
        titre = ecran.ids.titre_label
        anim = Animation(opacity=0, d=0) + Animation(opacity=1, y=titre.y + dp(6), d=0.35, t="out_quad") + Animation(y=titre.y, d=0.2)
        titre.opacity = 0
        anim.start(titre)

    def changer_theme(self):
        self.theme_cls.theme_style = "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        Snackbar(text=f"Thème: {self.theme_cls.theme_style}").open()

    def ouvrir_a_propos(self):
        if self.dialog:
            self.dialog.dismiss(force=True)
        self.dialog = MDDialog(
            title="À propos",
            text=("RG Musique\n\n"
                  "Télécharge et organise automatiquement les titres d'une playlist YouTube,\n"
                  "puis classe par artiste.\n\n"
                  "Front: KivyMD • Back: yt-dlp + mutagen"),
            buttons=[
                MDRaisedButton(text="Fermer", on_release=lambda *_: self.dialog.dismiss())
            ],
        )
        self.dialog.open()

    # --- Console & Progression ---
    def journal(self, msg: str):
        ecran = self.root.get_screen("principal")
        console = ecran.ids.console_label
        console.text += f"\n{msg}"
        def _resize(_):
            console.height = console.texture_size[1] + dp(20)
        Clock.schedule_once(_resize, 0.01)

    def definir_statut(self, texte: str):
        self.root.get_screen("principal").ids.statut_label.text = texte

    def definir_pourcent(self, valeur_float: float):
        valeur = max(0.0, min(100.0, float(valeur_float)))
        ecran = self.root.get_screen("principal")
        ecran.ids.barre_progression.value = valeur
        ecran.ids.pourcent_label.text = f"{int(valeur)}%"
        icone = ecran.ids.icone_spinner
        anim = Animation(scale=1.1, d=0.15) + Animation(scale=1.0, d=0.15)
        if not hasattr(icone, "scale"):
            icone.scale = 1.0
        anim.stop_all(icone)
        anim.start(icone)

    def definir_occupe(self, occupe: bool):
        ecran = self.root.get_screen("principal")
        ecran.ids.icone_spinner.disabled = not occupe
        ecran.ids.btn_dl.disabled = occupe

    # --- Bridge vers le backend ---
    def cliquer_telecharger(self):
        if self._telechargement_en_cours:
            Snackbar(text="Un téléchargement est déjà en cours…").open()
            return
        url = self.root.get_screen("principal").ids.url_playlist.text.strip()
        if not url:
            Snackbar(text="Colle l'URL de la playlist").open()
            return
        self.definir_occupe(True)
        self.definir_statut("Préparation…")
        self.definir_pourcent(0)
        self.journal("🚀 Lancement du téléchargement…")

        # Injection de la fonction de progression du backend
        tel_org.progression = self._hook_progression

        self._telechargement_en_cours = True
        self._travail = threading.Thread(target=self._telecharger_et_organiser, args=(url,), daemon=True)
        self._travail.start()

    def _hook_progression(self, d):
        status = d.get("status")
        if status == "downloading":
            percent_str = d.get("_percent_str", "0%")
            try:
                valeur = float(percent_str.replace("%", "").strip())
            except Exception:
                valeur = 0.0
            fichier = d.get("filename", "")
            Clock.schedule_once(lambda *_: self.definir_pourcent(valeur))
            Clock.schedule_once(lambda *_: self.definir_statut(f"Téléchargement… {percent_str}"))
            if fichier:
                Clock.schedule_once(lambda *_: self.journal(f"⬇️ {fichier} — {percent_str}"))
        elif status == "finished":
            fichier = d.get("filename", "")
            Clock.schedule_once(lambda *_: self.definir_statut("Conversion MP3…"))
            if fichier:
                Clock.schedule_once(lambda *_: self.journal(f"✅ Terminé: {fichier}"))

    def _telecharger_et_organiser(self, url: str):
        try:
            tel_org.telecharger_playlist(url)
            Clock.schedule_once(lambda *_: self.definir_pourcent(100))
            Clock.schedule_once(lambda *_: self.definir_statut("Organisation des musiques…"))
            Clock.schedule_once(lambda *_: self.journal("📂 Organisation des musiques…"))
            tel_org.organiser_musiques()
            Clock.schedule_once(lambda *_: self.journal("🎉 Terminé: Playlist rangée par artiste."))
            Clock.schedule_once(lambda *_: Snackbar(text="Terminé !").open())
        except Exception as e:
            Clock.schedule_once(lambda *_: self.journal(f"❌ Erreur: {e}"))
            Clock.schedule_once(lambda *_: self.definir_statut("Erreur"))
        finally:
            Clock.schedule_once(lambda *_: self.definir_occupe(False))
            self._telechargement_en_cours = False


if __name__ == "__main__":
    RGMusiqueApp().run()

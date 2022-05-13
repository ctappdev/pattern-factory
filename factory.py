# from fastapi import FastAPI
# from routers.router_virtualcontent import router as api_router
#
# app = FastAPI()
#
# app.include_router(api_router)

"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")


class ExporterFactory(ABC):
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a video expoerter"""

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a video expoerter"""


class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


FACTORIES = {
    "low": FastExporter(),
    "high": HighQualityExporter(),
    "master": MasterQualityExporter(),
}


def read_factory() -> ExporterFactory:
    while True:
        export_quality = input(
            f" What quality do you want({', '.join(FACTORIES)}): "
        )
        try:
            return FACTORIES[export_quality]
        except KeyError:
            print("Invalid selection")


def do_export(fac: ExporterFactory) -> None:
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    video_exporter.prepare_export("placeholder for video data")
    audio_exporter.prepare_export("placeholder for audio data")

    folder = pathlib.Path("/usr/temp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


print("=======> 1")
factory = read_factory()
do_export(factory)


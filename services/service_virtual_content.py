from models.model_virtualcontent import VirtualContent, VirtualContentModel
from abc import ABC, abstractmethod


class VirtualContentTransformer(ABC):

    @abstractmethod
    def do_transformation(self, payload: VirtualContent) -> VirtualContentModel:
        """Abstract transformation class"""


class GPosTransformer(VirtualContentTransformer):
    def do_transformation(self, payload: VirtualContent) -> VirtualContentModel:
        return VirtualContentModel.do_gpos_transformation(payload)


class EComTransfomer(VirtualContentTransformer):
    def do_transformation(self, payload: VirtualContent) -> VirtualContentModel:
        return VirtualContentModel.do_ecom_transformation(payload)


FACTORIES = {
    "gpos": GPosTransformer(),
    "ecom": EComTransfomer(),
}


async def do_virtual_content_transformation(parameters: VirtualContent) -> VirtualContentModel:
    try:
        fac: VirtualContentTransformer = FACTORIES[parameters.detail.tag]
        return fac.do_transformation(parameters)
    except KeyError:
        print("Invalid key")

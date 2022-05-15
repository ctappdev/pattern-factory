from models.model_virtualcontent import VirtualContentRequest, VirtualContentModel
from abc import ABC, abstractmethod


class VirtualContentTransformer(ABC):

    @abstractmethod
    def do_transformation(self, payload: VirtualContentRequest) -> VirtualContentModel:
        """Abstract transformation class"""


class GPosTransformer(VirtualContentTransformer):
    def do_transformation(self, payload: VirtualContentRequest) -> VirtualContentModel:
        return VirtualContentModel.do_gpos_transformation(payload)


class EComTransfomer(VirtualContentTransformer):
    def do_transformation(self, payload: VirtualContentRequest) -> VirtualContentModel:
        return VirtualContentModel.do_ecom_transformation(payload)


FACTORIES = {
    "GPOS": GPosTransformer(),
    "ECOM": EComTransfomer(),
}


async def do_virtualcontent_transformation(parameters: VirtualContentRequest) -> VirtualContentModel:
    try:
        fac: VirtualContentTransformer = FACTORIES[parameters.detail.channel]
        return fac.do_transformation(parameters)
    except KeyError:
        print("Invalid key")

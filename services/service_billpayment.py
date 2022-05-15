from models.model_billpayment import BillPaymentRequest, BillPaymentModel
from abc import ABC, abstractmethod


class BillPaymentTransformer(ABC):

    @abstractmethod
    def do_transformation(self, payload: BillPaymentRequest) -> BillPaymentModel:
        """Abstract transformation class"""


class GPosTransformer(BillPaymentTransformer):
    def do_transformation(self, payload: BillPaymentRequest) -> BillPaymentModel:
        return BillPaymentModel.do_gpos_transformation(payload)


class EComTransfomer(BillPaymentTransformer):
    def do_transformation(self, payload: BillPaymentRequest) -> BillPaymentModel:
        return BillPaymentModel.do_ecom_transformation(payload)


FACTORIES = {
    "GPOS": GPosTransformer(),
    "ECOM": EComTransfomer(),
}


async def do_billpayment_transformation(parameters: BillPaymentRequest) -> BillPaymentModel:
    try:
        fac: BillPaymentTransformer = FACTORIES[parameters.detail.channel]
        return fac.do_transformation(parameters)
    except KeyError:
        print("Invalid key")

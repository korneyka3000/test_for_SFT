from .models import CreditRequest


def get_producers_by_contract(contract_id: dict[str, int]):

    producers = (
        CreditRequest.objects
        .filter(contract_id=contract_id['id'])
        .prefetch_related('products')
        .values_list('products__producer_id', flat=True)
        .order_by('products__producer_id')
        .distinct()
    )

    return producers

def charge_with_retry(client, order):
    return client.charge(order.amount, idempotency_key=order.id)

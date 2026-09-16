# Billing retry change

The retry path now forwards the order's idempotency key to the billing provider. The developer claims this prevents duplicate charges after an accepted request times out.

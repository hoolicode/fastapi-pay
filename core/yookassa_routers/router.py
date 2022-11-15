from fastapi import APIRouter
from .checkout import checkout
from .payment import payment

router = APIRouter(prefix='/yookassa')
router.add_api_route('/checkout/', checkout, methods=['POST'])
router.add_api_route('/payment/', payment, methods=['POST'])

from fastapi import APIRouter
from .checkout import checkout

router = APIRouter(prefix='/yookassa')
router.add_api_route('/checkout/', checkout)

from app.core.celery_app import celery_app
from app.core.config import settings
from datetime import datetime, timedelta
from app.core.logger import logger
from app.helper.cache_manager import CacheManager, CacheDatabase


@celery_app.task(queue=settings.AUTH_SERVICE_QUEUE, acks_late=True)
def register_organization(payload):
    """

    :param payload:
    :return:
    """
    # steps to be performed upon registration
    # 1. Retrieving Roles info from the role_master index
    # 2. Create Organization
    # 3. Create OrganizationSubscription & OrganizationSubscriptionPayment records
    # 4. Create Organization Owner user
    pass

"""
In this pytest plugin we will keep all our pytest marks used in our tests and
all related hooks/plugins to markers.
"""
import os

import pytest
from funcy import compose

from ocs_ci.framework import config
from ocs_ci.ocs.constants import (
    ORDER_BEFORE_OCS_UPGRADE,
    ORDER_BEFORE_OCP_UPGRADE,
    ORDER_BEFORE_UPGRADE,
    ORDER_OCP_UPGRADE,
    ORDER_OCS_UPGRADE,
    ORDER_AFTER_OCP_UPGRADE,
    ORDER_AFTER_OCS_UPGRADE,
    ORDER_AFTER_UPGRADE,
)

# tier marks

tier1 = pytest.mark.tier1(value=1)
tier2 = pytest.mark.tier2(value=2)
tier3 = pytest.mark.tier3(value=3)
tier4 = pytest.mark.tier4(value=4)
tier4a = compose(tier4, pytest.mark.tier4a)
tier4b = compose(tier4, pytest.mark.tier4b)
tier4c = compose(tier4, pytest.mark.tier4c)
tier_after_upgrade = pytest.mark.tier_after_upgrade(value=5)

tier_marks = [
    tier1, tier2, tier3, tier4, tier4a, tier4b, tier4c, tier_after_upgrade,
]

# build acceptance
acceptance = pytest.mark.acceptance

# team marks

e2e = pytest.mark.e2e
ecosystem = pytest.mark.ecosystem
manage = pytest.mark.manage
libtest = pytest.mark.libtest

team_marks = [manage, ecosystem, e2e]

# components  and other markers
ocp = pytest.mark.ocp
rook = pytest.mark.rook
ui = pytest.mark.ui
csi = pytest.mark.csi
monitoring = pytest.mark.monitoring
workloads = pytest.mark.workloads
performance = pytest.mark.performance
scale = pytest.mark.scale
deployment = pytest.mark.deployment
polarion_id = pytest.mark.polarion_id
bugzilla = pytest.mark.bugzilla

# upgrade related markers
# Requires pytest ordering plugin installed
# Use only one of those marker on one test case!
order_pre_upgrade = pytest.mark.run(order=ORDER_BEFORE_UPGRADE)
order_pre_ocp_upgrade = pytest.mark.run(order=ORDER_BEFORE_OCP_UPGRADE)
order_pre_ocs_upgrade = pytest.mark.run(order=ORDER_BEFORE_OCS_UPGRADE)
order_ocp_upgrade = pytest.mark.run(order=ORDER_OCP_UPGRADE)
order_ocs_upgrade = pytest.mark.run(order=ORDER_OCS_UPGRADE)
order_post_upgrade = pytest.mark.run(order=ORDER_AFTER_UPGRADE)
order_post_ocp_upgrade = pytest.mark.run(order=ORDER_AFTER_OCP_UPGRADE)
order_post_ocs_upgrade = pytest.mark.run(order=ORDER_AFTER_OCS_UPGRADE)
ocp_upgrade = compose(pytest.mark.ocp_upgrade, order_ocp_upgrade)
ocs_upgrade = compose(pytest.mark.ocs_upgrade, order_ocs_upgrade)
pre_upgrade = compose(pytest.mark.pre_upgrade, order_pre_upgrade)
pre_ocp_upgrade = compose(pytest.mark.pre_ocp_upgrade, order_pre_ocp_upgrade)
pre_ocs_upgrade = compose(pytest.mark.pre_ocs_upgrade, order_pre_ocs_upgrade)
post_upgrade = compose(pytest.mark.post_upgrade, order_post_upgrade)
post_ocp_upgrade = compose(pytest.mark.post_ocp_upgrade, order_post_ocp_upgrade)
post_ocs_upgrade = compose(pytest.mark.post_ocs_upgrade, order_post_ocs_upgrade)

# mark the test class with marker below to ignore leftover check
ignore_leftovers = pytest.mark.ignore_leftovers

# testing marker this is just for testing purpose if you want to run some test
# under development, you can mark it with @run_this and run pytest -m run_this
run_this = pytest.mark.run_this

# Skipif marks
google_api_required = pytest.mark.skipif(
    not os.path.exists(os.path.expanduser(
        config.RUN['google_api_secret'])
    ), reason="Google API credentials don't exist"
)

aws_platform_required = pytest.mark.skipif(
    config.ENV_DATA['platform'].lower() != 'aws',
    reason="Tests are not running on AWS deployed cluster"
)

vsphere_platform_required = pytest.mark.skipif(
    config.ENV_DATA['platform'].lower() != 'vsphere',
    reason="Tests are not running on VSPHERE deployed cluster"
)

ipi_deployment_required = pytest.mark.skipif(
    config.ENV_DATA['deployment_type'].lower() != 'ipi',
    reason="Tests are not running on IPI deployed cluster"
)

# Filter warnings
filter_insecure_request_warning = pytest.mark.filterwarnings(
    'ignore::urllib3.exceptions.InsecureRequestWarning'
)

# collect Prometheus metrics if test fails with this mark
# specify Prometheus metric names in argument
gather_metrics_on_fail = pytest.mark.gather_metrics_on_fail

# here is the place to implement some plugins hooks which will process marks
# if some operation needs to be done for some specific marked tests.

# Marker for skipping tests based on OCS version
skipif_ocs_version = pytest.mark.skipif_ocs_version

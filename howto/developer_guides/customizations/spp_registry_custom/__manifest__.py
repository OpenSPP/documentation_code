# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenSPP Registry: Customization",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/openspp/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": ["openspp_dev"],
    "depends": [
        "g2p_registry_group",
        "g2p_registry_individual",
        "g2p_registry_membership",
        "spp_custom_field",
    ],
    "data": [
        "views/group_membership_views.xml",
        "views/individual_views.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False,
}

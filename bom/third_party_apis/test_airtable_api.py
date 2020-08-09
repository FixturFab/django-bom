import pytest
from pytest_factoryboy import register

from airtable import Airtable

from ..helpers import create_some_fake_parts, create_user_and_organization
from ..models import ManufacturerPart, Part, SellerPart
from . import airtable_api


def test_get_existing_manufacturer_id():
    manufacturer_id = airtable_api.get_manufacturer_id("Keystone Electronics")
    exp_id = "recuI9DyolfWew2yj"
    assert manufacturer_id == exp_id


def test_get_new_manufacturer_id():
    mfg_name = "GenericTestManufacturerNameDONOTUSE"
    manufacturer_id = airtable_api.get_manufacturer_id(mfg_name)

    manufacturer = Airtable(airtable_api.OPERATIONS_ID, "Manufacturers")
    result = manufacturer.get(manufacturer_id)
    assert result is not None
    manufacturer.delete(manufacturer_id)
    assert result['fields']['Name'] == mfg_name


def test_get_existing_supplier_id():
    supplier_id = airtable_api.get_supplier_id("Digikey")
    exp_id = "recUwVqcEeI4N8RA6"
    assert supplier_id == exp_id


def test_get_new_supplier_id():
    mfg_name = "GenericSupplierNameDONOTUSE"
    supplier_id = airtable_api.get_supplier_id(mfg_name)

    supplier = Airtable(airtable_api.OPERATIONS_ID, "Suppliers")
    result = supplier.get(supplier_id)
    assert result is not None
    supplier.delete(supplier_id)
    assert result['fields']['Name'] == mfg_name


@pytest.mark.django_db
def test_add_new_mfg_part():
    user, org = create_user_and_organization()
    create_some_fake_parts(org)
    mfg_part = ManufacturerPart.objects.first()
    created_id = airtable_api.add_mfg_part(mfg_part)

    manufacturer_parts = Airtable(airtable_api.OPERATIONS_ID, "Manufacturer Parts")
    result = manufacturer_parts.get(created_id)
    assert result is not None
    manufacturer_parts.delete(created_id)


@pytest.mark.django_db
def test_add_part():
    user, org = create_user_and_organization()
    create_some_fake_parts(org)
    part = Part.objects.first()
    part_id = airtable_api.add_part(part)

    inventory = Airtable(airtable_api.OPERATIONS_ID, "Inventory")
    result = inventory.get(part_id)
    assert result is not None
    inventory.delete(part_id)

'''
test_rrsig_signer_match - Tests rrsig_signer_match validator.

.. Copyright (c) 2015 Neustar, Inc. All rights reserved.
.. See COPYRIGHT.txt for full notice.  See LICENSE.txt for terms and conditions.
'''
# pylint: skip-file


import dns_sprockets_lib.validators.tests.harness as harness


def test_rrsig_signer_match():

    (tests, errs) = harness.test_validator(
        test_name='rrsig_signer_match',
        zone_name='example',
        file_name='rfc4035_example.')
    assert tests == 27
    assert errs == 0

    (tests, errs) = harness.test_validator(
        test_name='rrsig_signer_match',
        zone_name='example',
        file_name='rfc5155_example.')
    assert tests == 30
    assert errs == 0

    (tests, errs) = harness.test_validator(
        test_name='rrsig_signer_match',
        zone_name='001.cst.net',
        file_name='001.cst.net.')
    assert tests == 11
    assert errs == 0

    (tests, errs) = harness.test_validator(
        test_name='rrsig_signer_match',
        zone_name='001.cst.net',
        file_name='001.cst.net._bad_rrsig_signer')
    assert tests == 11
    assert errs == 1

# end of file


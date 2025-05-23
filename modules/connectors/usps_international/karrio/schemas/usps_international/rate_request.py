import attr
import jstruct
import typing


@attr.s(auto_attribs=True)
class RateRequestType:
    originZIPCode: typing.Optional[str] = None
    foreignPostalCode: typing.Optional[str] = None
    destinationCountryCode: typing.Optional[str] = None
    weight: typing.Optional[int] = None
    mailingDate: typing.Optional[str] = None
    length: typing.Optional[int] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    priceType: typing.Optional[str] = None
    mailClass: typing.Optional[str] = None
    accountType: typing.Optional[str] = None
    accountNumber: typing.Optional[str] = None
    itemValue: typing.Optional[int] = None
    extraServices: typing.Optional[typing.List[int]] = None

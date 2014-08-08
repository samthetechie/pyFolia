#!/usr/bin/python
# coding: utf8

from .keys import *
from .ip import Ip
from .osm import Osm
from .bing import Bing
from .nokia import Nokia
from .yahoo import Yahoo
from .tomtom import Tomtom
from .google import Google
from .arcgis import Arcgis
from .reverse import Reverse
from .geonames import Geonames
from .mapquest import Mapquest
from .timezone import Timezone
from .elevation import Elevation
from .geolytica import Geolytica
from .canadapost import Canadapost


def yahoo(location):
    """
    # Yahoo

    Yahoo PlaceFinder is a geocoding Web service that helps developers make
    their applications location-aware by converting street addresses or
    place names into geographic coordinates (and vice versa).
    Using Geocoder you can retrieve Yahoo's geocoded data from Yahoo BOSS Geo Services.

    ## Python Example

        >>> import geocoder # pip install geocoder
        >>> g = geocoder.yahoo('<address>')
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * country
        * county
        * lat
        * lng
        * locality
        * location
        * neighborhood
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number

    ## Parameters

        * :param ``location``: Your search location you want geocoded.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Yahoo BOSS Geo Services](https://developer.yahoo.com/boss/geo/)

    """
    return Yahoo(location)

def geolytica(location):
    """
    # Geolytica

    Geocoder.ca - A Canadian and US location geocoder.
    Using Geocoder you can retrieve Geolytica's geocoded data from Geocoder.ca.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.geolytica(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * lat
        * lng
        * locality
        * location
        * postal
        * provider
        * route
        * state
        * status
        * street_number

    ## Parameters

        * :param location: Your search location you want geocoded.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Geocoder.ca](http://geocoder.ca/?api=1)

    """
    return Geolytica(location)

def arcgis(location):
    """
    # ArcGIS

    The World Geocoding Service finds addresses and places in all supported countries
    from a single endpoint. The service can find point locations of addresses,
    business names, and so on.  The output points can be visualized on a map,
    inserted as stops for a route, or loaded as input for a spatial analysis.
    an address, retrieving imagery metadata, or creating a route.
    Using Geocoder you can retrieve ArcGIS's geocoded data from ArcGIS REST API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.arcgis('<address>') # pip install geocoder
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * bbox
        * lat
        * lng
        * location
        * provider
        * quality
        * status

    ## Parameters

        * :param ``location``: Your search location you want geocoded.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [ArcGIS REST API](https://developers.arcgis.com/rest/geocode/api-reference/geocoding-find.htm)

    """
    return Arcgis(location)

def bing(location, key=bing_key):
    """
    # Bing

    The Bing Maps REST Services Application Programming Interface (API)
    provides a Representational State Transfer (REST) interface to perform
    tasks such as creating a static map with pushpins, geocoding an address,
    retrieving imagery metadata, or creating a route.
    Using Geocoder you can retrieve Bing's geocoded data from Bing Maps REST Services.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.bing(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * country
        * lat
        * lng
        * locality
        * location
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * status_description

    ## Parameters

        * :param location: Your search location you want geocoded.
        * :param key: (optional) use your own API Key from Bing.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Bing Maps REST Services](http://msdn.microsoft.com/en-us/library/ff701714.aspx)

    """
    return Bing(location, key=key)

def nokia(location, app_id=app_id, app_code=app_code):
    """
    # Nokia

    Send a request to the geocode endpoint to find an address using a combination of
    country, state, county, city, postal code, district, street and house number.
    Using Geocoder you can retrieve Nokia's geocoded data from HERE Geocoding REST API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.nokia(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * accuracy
        * address
        * bbox
        * country
        * county
        * lat
        * lng
        * locality
        * location
        * neighborhood
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number

    ## Parameters

        * :param location: Your search location you want geocoded.
        * :param app_code: (optional) use your own Application Code from Nokia.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [HERE Geocoding REST API](https://developer.here.com/rest-apis/documentation/geocoder)

    """
    return Nokia(location, app_id=app_id, app_code=app_code)

def tomtom(location, key=tomtom_key):
    """
    # TomTom

    The Geocoding API gives developers access to TomTom’s first class geocoding service.
    Developers may call this service through either a single or batch geocoding request.
    This service supports global coverage, with house number level matching in over 50 countries,
    and address point matching where available.
    Using Geocoder you can retrieve TomTom's geocoded data from Geocoding API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.tomtom(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * country
        * lat
        * lng
        * locality
        * location
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number

    ## Parameters

        * :param location: Your search location you want geocoded.
        * :param key: (optional) use your own API Key from TomTom.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Geocoding API](http://developer.tomtom.com/products/geocoding_api)

    """
    return Tomtom(location, key=key)

def mapquest(location):
    """
    # MapQuest

    The geocoding service enables you to take an address and get the
    associated latitude and longitude. You can also use any latitude
    and longitude pair and get the associated address. Three types of
    geocoding are offered: address, reverse, and batch.
    Using Geocoder you can retrieve MapQuest's geocoded data from Geocoding Service.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.mapquest(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * country
        * lat
        * lng
        * locality
        * location
        * postal
        * provider
        * quality
        * state
        * status

    ## Parameters

        * :param location: Your search location you want geocoded.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Geocoding Service](http://www.mapquestapi.com/geocoding/)

    """
    return Mapquest(location)

def osm(location):
    """
    # OSM

    Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
    and address and to generate synthetic addresses of OSM points (reverse geocoding).
    Using Geocoder you can retrieve OSM's geocoded data from Nominatim.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.osm(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * bbox
        * country
        * lat
        * lng
        * locality
        * location
        * neighborhood
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number
        * suburb

    ## Parameters

        * :param location: Your search location you want geocoded.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Nominatim](http://wiki.openstreetmap.org/wiki/Nominatim)

    """
    return Osm(location)

def google(location, short_name=True):
    """
    # Google

    Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway,
    Mountain View, CA") into geographic coordinates (like latitude 37.423021 and
    longitude -122.083739), which you can use to place markers or position the map.
    Using Geocoder you can retrieve Google's geocoded data from Google Geocoding API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.google(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * accuracy
        * address
        * bbox
        * country
        * county
        * lat
        * lng
        * locality
        * location
        * neighborhood
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number
        * sublocality

    ## Parameters

        * :param location: Your search location you want geocoded.
        * :param short_name: (optional) if ``False`` will retrieve the results with Long names.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/)

    """
    return Google(location, short_name=short_name)

def ip(location):
    """
    # IP Address

    MaxMind's GeoIP2 products enable you to identify the location,
    organization, connection speed, and user type of your Internet
    visitors. The GeoIP2 databases are among the most popular and
    accurate IP geolocation databases available. Using Geocoder you
    can retrieve IP Address's geocoded data from MaxMind's GeoIP2.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.ip(<IP Address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * city
        * continent
        * country
        * domain
        * ip
        * isp
        * lat
        * lng
        * location
        * postal
        * provider
        * state
        * status

    ## Parameters

        * :param location: Your search IP Address you want geocoded.
        * :param location: (optional) if left blank will return your current IP address's location.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [MaxMind's GeoIP2](https://www.maxmind.com/en/geolocation_landing)

    """
    return Ip(location)

def timezone(location, timestamp=''):
    """
    # TimeZone

    The Time Zone API provides time offset data for locations on the surface of the earth.
    Requesting the time zone information for a specific Latitude/Longitude pair will
    return the name of that time zone, the time offset from UTC, and the Daylight Savings offset.
    Using Geocoder you can retrieve TimeZone's geocoded data from Google Time Zone API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.timezone('<address or [lat,lng]>')
        >>> g.timezone
        'Eastern Daylight Time'
        ...

    ## Geocoder Attributes

        * dst
        * lat
        * lng
        * location
        * provider
        * status
        * timestamp
        * timezone
        * timezone_id
        * utc

    ## Parameters

        * :param ``location``: Your search location you want geocoded.
        * :param ``timestamp``: (optional) specifies the desired time as seconds

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Google Time Zone API](https://developers.google.com/maps/documentation/timezone/)

    """
    return Timezone(location)

def elevation(location):
    """
    # Elevation

    The Elevation API provides elevation data for all locations on the surface of the
    earth, including depth locations on the ocean floor (which return negative values).
    In those cases where Google does not possess exact elevation measurements at the
    precise location you request, the service will interpolate and return an averaged
    value using the four nearest locations.

    Using Geocoder you can retrieve Elevation's geocoded data from Google Elevevation API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.elevation('<address or [lat,lng]>')
        >>> g.meters
        48.5
        ...

    ## Geocoder Attributes

        * address
        * elevation
        * feet
        * lat
        * lng
        * location
        * meters
        * provider
        * resolution
        * status

    ## Parameters

        * :param ``location``: Your search location you want geocoded.
        * :param ``location``: (input) can be specified as [lat, lng].

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Google Elevevation API](https://developers.google.com/maps/documentation/elevation/)

    """
    return Elevation(location)

def reverse(location, short_name=True):
    """
    # Reverse

    The term geocoding generally refers to translating a human-readable address into
    a location on a map. The process of doing the opposite, translating a location
    on the map into a human-readable address, is known as reverse geocoding.
    Using Geocoder you can retrieve Reverse's geocoded data from Google Geocoding API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.reverse(['lat','lng'])
        >>> g.address
        '453 Booth Street, Ottawa'
        ...

    ## Geocoder Attributes

        * accuracy
        * address
        * bbox
        * country
        * county
        * lat
        * lng
        * locality
        * location
        * neighborhood
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number
        * sublocality

    ## Parameters

        * :param ``location``: Your search location you want geocoded.
        * :param ``short_name``: (optional) if ``False`` will retrieve the results with Long names.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/)

    """
    return Reverse(location)

def canadapost(location, country='CA', key=''):
    """
    # CanadaPost

    The next generation of address finders, AddressComplete uses intelligent, fast
    searching to improve data accuracy and relevancy. Simply start typing a business
    name, address or Postal Code and AddressComplete will suggest results as you go.
    Using Geocoder you can retrieve CanadaPost's geocoded data from Addres Complete API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.canadapost('<address>')
        >>> g.postal
        'K1R 7K9'
        ...

    ## Geocoder Attributes

        * address
        * country
        * key
        * locality
        * location
        * ok
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number

    ## Parameters

        * :param ``location``: Your search location you want geocoded.
        * :param ``key``: (optional) use your own API Key from CanadaPost Address Complete.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Addres Complete API](https://www.canadapost.ca/pca/)

    """
    return Canadapost(location, country=country, key=key)

def geonames(location, username='addxy'):
    """
    # GeoNames

    GeoNames is mainly using REST webservices. Find nearby postal codes / reverse geocoding
    This service comes in two flavors.You can either pass the lat/long or a postalcode/placename.

    Using Geocoder you can retrieve GeoNames's geocoded data from GeoNames REST Web Services.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.geonames('<address>')
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * country
        * lat
        * lng
        * location
        * population
        * provider
        * quality
        * state
        * status

    ## Parameters

        * :param ``location``: Your search location you want geocoded.
        * :param ``username``: (required) needs to be passed with each request.

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [GeoNames REST Web Services](http://www.geonames.org/export/web-services.html)

    """
    return Geonames(location, username=username)

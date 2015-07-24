# whosonfirst-placetypes

## Who is on first?

For any hierarchy there are three classes of place type:

* Common (C) – these are, well, common across *any* hierarchy for any place in a gazetteer

* Common-optional (CO) – these are meant to be part of a common hierarchy but may not be present because they aren't relevant or because we don't have the data (for example, the building for a venue)

* Optional (O) – these are the parts of a hierarchy specific to a location, for example the many nested "departments" in France or Germany. The only rule is that an optional (O) place type has to fit somewhere inside the common (C) hierarchy.

So the minimum list of place types for a skeleton hierarchy, applied globally, would be:

``` 
- continent (C)
  - empire (CO)
    - country (C)
      - region (C)
        - "county" (CO)
        - "metro area" (CO)
          - locality (C)
	    - macrohood (O)
              - neighbourhood (C)
	        - microhood (O)
                  - campus –  (CO)
                    - building – (CO)
                      - address – (CO)
                        - venue (C)
```

We can add others that slot in somewhere on that tree but this is the skeleton.

For example a [microhood](http://aaronland.info/minitenders/) would be parented by a 
neighbourhood. Each one of these places types would like the places 
they represent have a stable numeric identifier.

## Dispute

TBW

## Placetypes

All place types have a unique 64-bit numeric ID. It should always be possible to query or filter for places by that numeric ID so that the burden of remembering whether it is `neighbourhood` or `neighborhood` or `quartier` or whatever is reserved for friendly banter over drinks.

In alphabetical order the current list of placetypes in Who's On First is:

### address

`102312329`

Yeah, so like "metro areas" this is an open question. The question being: How/what do we do with OpenAddresses? Neither Kelso or I aren't sure of anything except maybe to put this here as a placeholder for probably between buildings and venues

### building

See also: [Imagining the Built Works Registry](https://builtworksregistry.wordpress.com/imagining-the-built-works-registry-by-aaron-straup-cope-christine-kuan/)

### campus

Things like universities or office complexes. Probably airports.

### continent

I think we're all in pretty broad agreement about continents, yeah?

### country

Basically places that issue passports, notwithstanding the details (like
empires which actually issue the passports...)

### county

This needs a better - that is more abstract - name. Like "region" instead of state, province, whatever... but for counties.

### dependency

It's not a sub-region of a country but rather dependent on a parent country for defence, passport control, subsidies, etc.

### disputed

Places that one or more parties claim as their own. As of this writing _all_ disputed places are parented only by the country (and higher) IDs of the claimants. This isn't to say there aren't more granular hierarchies to be applied to these place only that we are starting with the simple stuff first.

### empire

Or "sovereignty" but really... empire. For example the Meta United States that contains both the US and Puerto Rico.

### locality

Towns and cities, independent of size or population. Things with neighbourhoods, basically. We can start with Quattroshapes and then WOE and then the OSM extracts for things without geometries.

### macrohood

Like "BoCoCa" which in WOE is a neighbourhood that parents another... neighbourhood.

### metroarea

Things like "The Bay Area" – this one is hard so we shouldn't spend too much time worrying about the details yet but instead treat as something we want to do eventually. We can start with the Natural Earth "urban areas" and maybe some other parts of NE.

### microhood

Because all place is disputed. And everyone has a name for a place that will offend someone else.

### neighbourhood

Things no one will agree on. Ever.

### region

States, provinces, regions. Let's just call them regions. Places that would have
a bone in a "states rights" argument. 

### venue

Things with walls, basically. Things with walls that might be public (a bar) or private (your apartment) by default.

## Hierarchies

A Who's On First (`wof:`) hierarchy is a list of dictionaries, which each item is a dictionary containing a full hierarchy. Like this:

```
"wof:hierarchy": [
	{ "neighbourhood_id": 9997, "locality_id": 9997, "metro_id": 9998, "county_id": 9998, "region_id": 9998, "country_id": 9998, "continent_id": 9998 },
	{ "neighbourhood_id": 9997, "locality_id: 9997, "metro_id": 9999, "county_id": 9999, "region_id": 9999, "country_id": 9999, "continent_id": 9999 }
]
```

See below for details and rationale.

### How did we get here?

_The following is a verbatim written exercise to work through the issue of how a hierarchy should be represented or, more specifically, how the potentially multiple hierarchies that a given place might encompass should be represented._

Something something something as elements on the root `properties` dictionary. Like this:

```
{
	"wof:neighbourhood_id": 9999,
	"wof:locality_id": 9999,
	"wof:county_id": 9999,
	"wof:region_id": 9999,
	"wof:country_id": 9999,
	"wof:continent_id": 9999
}
```

Something something something as a dictionary on the root `properties` dictionary. Like this:
 
```
"wof:hierarchy": {
	"neighbourhood_id": 9999,
	"locality_id": 9999,
	"county_id": 9999,
	"region_id": 9999,
	"country_id": 9999,
	"continent_id": 9999
}
```

This has the advantage of keeping all the hierarchy information in one place however it is left as an exercise to the user to enforce the actual order of the hierarchy since there is no way to be certain that `programming langage X` will ensure the ordering of the dictionary keys. We could define the hierarchy as a list of dictionaries which would allow to explicitly encode the parent for that node but those extra bytes in each record will add up fast when dealing with a global hierarchy. Like this:

```
"wof:hierarchy": [
	{ "neighbourhood_id": 9999, "parent": "locality_id" },
	{ "locality_id": 9999, "parent: "county_id" },
	{ "county_id": 9999, "parent": "region_id" },
	{ "region_id": 9999, "parent": "country_id" },
	{ "country_id": 9999, "parent": "continent_id" },
	{ "continent_id": 9999, "parent": "" }
}
```

Meanwhile we also know that we want to support certain place types that will have multiple parents (because geography) like metropolitain areas or, if we choose to include them in the gazetteer proper, road networks.

At a minimum this means that some of the values for placetypes have to be lists which probably means _all_ of the values should be lists so that people don't have to think about context or test data types. For example:

```
"wof:hierarchy": {
	"neighbourhood_id": [ 9999 ],
	"locality_id": [ 9999 ],
	"metropolitain_area": [ 9999 ],
	"county_id": [ 9999, 9999 ],
	"region_id": [ 9999 ],
	"country_id": [ 9999 ],
	"continent_id": [ 9999 ],
}
```

However, it is possible to imagine a place type with not only multiple parents but multiple ancestors. A timezone or, again, a road network. In which case you find yourself with a dictionary whose values are lists of dictionaries. At which point you risk spiralling off in to Semantic Web graph theory quicksand.

So maybe the thing to do is suffer mixed content (unique IDs and lists) where the rule is the immediate (outer) hierarchy stops the moment there are multiple parents. Like this:

```
"wof:hierarchy": {
	"neighbourhood_id": 9999,
	"locality_id": 9999,
	"metro_id": [
		{ "metro_id": 9998, "county_id": 9998, "region_id": 9998, "country_id": 9998, "continent_id": 9998 },
		{ "metro_id": 9999, "county_id": 9999, "region_id": 9999, "country_id": 9999, "continent_id": 9999 }
	]
}
```

Or maybe the hierarchy is always just a list of dictionaries, each containing a full hierarchy. Like this:

```
"wof:hierarchy": [
	{ "neighbourhood_id": 9997, "locality_id": 9997, "metro_id": 9998, "county_id": 9998, "region_id": 9998, "country_id": 9998, "continent_id": 9998 },
	{ "neighbourhood_id": 9997, "locality_id: 9997, "metro_id": 9999, "county_id": 9999, "region_id": 9999, "country_id": 9999, "continent_id": 9999 }
]
```

Reasons why this last suggestion is good:

* It is explicit
* It is easy to compare multiple hierarchies
* It doesn't require the user do a lot of mental arithmetic to construct the complete hierarchy or to support whatever "efficiencies" we dream up in the moment
* It is easier to change going forward (say before an "official" launch) than the alternatives

Reasons why this last suggestion is, or might be, bad:

* If we support metropolitain areas then many places (localities, neighbourhood, venues) may have multiple hierarchies where the only difference will (likely) be the county, leaving all the remaining ancestors in common
* File size, disk space and bandwidth - this is the corollary of the first point and akin to whitespace or coordinates with > 6 decimal points in GeoJSON files

In the end the "good" reasons outweighed the "bad" reasons.

## See also

* https://github.com/mapzen/py-mapzen-whosonfirst-placetypes

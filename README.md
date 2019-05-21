[![Stability](https://img.shields.io/badge/Stability-Under%20Active%20Development-Red.svg)](https://github.com/pbs/vanna-python-client)

# Warning: Under Active Development

This library is under active development and likely to change further before
stabilizing.

# Vanna Python Client

`vanna` is a feature flagging library we use at [PBS](http://pbs.org). It helps
us deliver new features or refactor existing ones quickly and safely.

## Getting Started

We can install the `vanna` client via PyPI.

```sh
pip install vanna
```

After installing, you can import and setup the client.

```py
import vanna

client = vanna.Client(features=[
    vanna.Feature(
        id="your-feature-id",
        type=vanna.FeatureType.Boolean,
        value=True
    )
])

is_feature_enabled = client.variation("your-feature-slug")
if (is_feature_enabled):
    print("Feature is enabled!")
else:
    print("Feature is disabled!")
```

## API

`vanna`'s API surface consists of: `Feature` and `Client`. `Clients` can contain
a list of `Features` and is the main API to interact with the library.

```py
# TODO
```

### Features

---

A feature is the idea of attribute that you're considering changing in your
application. It could be something small like `new-button-styles` or something
big like `new-website-v2`. We can instantiate a feature via the `Feature` class.

```py
feature = vanna.Feature(
    id="your-feature-id",
    type=vanna.FeatureType.Boolean,
    value=True,
    targets=["alpha-users"]
)
```

#### `id`

Id is the identifier/name for a particular feature. It will be a referenced when
you call `client.variation`.

#### `type`

Type can be one of the following values: `boolean`, `percentage`.

A `boolean` feature will be either turned on/off depending on the users. A
`percentage` feature will be turned on/off depending on the users as well as a
seeded random number generator.

#### `value`

Value is a boolean value for your feature. This is the value that
`client.variation` will resolve to _if_ the user matches the parameter passed
into the feature client. Conversely if the user does _not_ match the parameter
of passed into the feature client, `client.variation` will resolve to
`not value`.

#### `targets`

Target is an optional parameter of a feature that will limit the scope of the
feature matching. If we declare a list of user types in a feature `target`,
`client.variation` will only resolve the `value` of the feature _if_ the
`target` passed into the client matches one of the feature's `targets`. If a
target is not present in a particular feature, it's assumed that the feature
targets all users.

### Clients

---

To tie the idea of features and sources together, we finally get to clients.
Clients are the main way that most of your application code will interact with
`vanna`.

#### `FeatureClient`

The feature client can be setup with the following parameters. Once setup, we
can get whether a feature is enabled via `client.variation`, which will return a
boolean value.

```py
import vanna

client = vanna.Client(
  features=[],
  user_id="u123",
  target="beta-tester"
)

is_enabled = client.variation("some-feature")
```

#### `features`

Features holds a list of, well, features.

#### `user_id`

A unique user identifier that will be required if a feature is of type
`percentage`. If the user is an anonymous user, you have to supply a hard-coded
`userId` or generate a unique fingerprint.

#### `target`

A target is a string that describes the user role or group of the user. It will
be used to match against a feature's `target` to determine if a feature applies
to a particular user.

## Rationale

To learn more about the rationale behind using feature flags, read these
articles:

- https://martinfowler.com/articles/feature-toggles.html
- https://blog.travis-ci.com/2014-03-04-use-feature-flags-to-ship-changes-with-confidence/

## Licensing

[MIT](/LICENSE)

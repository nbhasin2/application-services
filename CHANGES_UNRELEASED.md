**See [the release process docs](docs/howtos/cut-a-new-release.md) for the steps to take when cutting a new release.**

# Unreleased Changes

[Full Changelog](https://github.com/mozilla/application-services/compare/v0.53.2...master)

## Rust

### What's New

- Sourcing `libs/bootstrap-desktop.sh` is not a thing anymore. Please run `./libs/verify-desktop-environment.sh` at least once instead. ([#2769](https://github.com/mozilla/application-services/pull/2769))

## Android

### What's changed

- There is now preliminary support for an "autoPublish" local-development workflow similar
  to the one used when working with Fenix and android-components; see
  [this howto guide](./docs/howtos/locally-published-components-in-fenix.md) for details.

## Push

### Breaking changes

- Android: The `PushManager.verifyConnection` now returns a `List<PushSubscriptionChanged>` that contain the channel ID and scope of the subscriptions that have expired. ([#2632](https://github.com/mozilla/application-services/pull/2632))
  See [`onpushsubscriptionchange`][0] events on how this change can be propagated to notify web content.

[0]: https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/onpushsubscriptionchange

## Places

### What's fixed

- Improve handling of tags for bookmarks with the same URL. These bookmarks no
  longer cause syncs to fail ([#2750](https://github.com/mozilla/application-services/pull/2750)),
  and bookmarks with duplicate or mismatched tags are reuploaded
  ([#2774](https://github.com/mozilla/application-services/pull/2774)).

# How to contribute

Diverse contributions are essential for keeping Who's On First great. The world is a very big place, and it keeps changing. We want to keep it as easy as possible to contribute open data about your part of the world (or your favorite part of the world). There are a few guidelines that we need contributors to follow so that we can have a chance of keeping on top of things.

At this stage, we encourage you to [submit issues](https://github.com/whosonfirst/whosonfirst-data/issues/new) you find with the data rather than getting your Octocat on. If you don't know what that means: really - just submit a GitHub Issue.

## Getting started

* Make sure you have a [GitHub account](https://github.com/signup/free)
* Optional: Get a [Mapzen developer account](https://mapzen.com/developers/sign_in)
* Submit a ticket for your issue, assuming one does not already exist.
  * Clearly describe the issue including steps to reproduce when it is a bug.
  * If you are recommending a solution, please include as many references as possible.
  * If you propose importing or adding concordance with open data, say where the data comes from with a download link and license link.

## Making changes

* Fork the [whosonfirst-data](https://github.com/whosonfirst/whosonfirst-data) repository on GitHub. We're using GitHub and git today, maybe that will change in the future. More about that [over there](https://github.com/whosonfirst/whosonfirst-data/blob/master/README.md#git-and-github).
* Create a topic branch from where you want to base your work.
  * This is usually the master branch.
  * Only target release branches if you are certain your fix must be on that
    branch.
  * To quickly create a topic branch based on master; `git checkout -b
    fix/master/my_contribution master`. Please avoid working directly on the
    `master` branch.
* Documentation about names, placetypes, dates, and more is in the [See also-er](https://github.com/whosonfirst/whosonfirst-data/blob/master/CONTRIBUTING.md#see-also-er) section below.
* Make commits of logical units.
* Check for unnecessary whitespace with `git diff --check` before committing.
* Make sure your commit messages are in the proper format.

````
    (Issue Number) Make the example in CONTRIBUTING imperative and concrete

    Description of the existing behavior without the patch, why this is
    a problem, and how the patch fixes the problem when applied.

````

The first line is a real-life imperative statement with a ticket number from the issue tracker.  The body is your place to provide more detail.

Tests aren't included, yet. Someday:

* Make sure you have added the necessary tests for your changes.
* Run _all_ the tests to assure nothing else was accidentally broken.

## Making Trivial Changes

### Documentation

For changes of a trivial nature to comments and documentation, it is not
always necessary to create a new issue in GitHub. In this case, it is
appropriate to start the first line of a commit with '(doc)' instead of
a ticket number.

````
    (doc) Add documentation commit example to CONTRIBUTING

    There is no example for contributing a documentation commit
    to the Who's On First repository. This is a problem because the
    contributor is left to assume how a commit of this nature may appear.

````

The first line is a real-life imperative statement with '(doc)' in place of what would have been the ticket number in a non-documentation related commit. The body describes the nature of the new documentation or comments added.


## Submitting Changes

* Push your changes to a topic branch in your fork of the repository.
* Submit a pull request to the repository in the whosonfirst organization.
* Update your GitHub issue to mark that you have submitted code and are ready for it to be reviewed (Status: Ready for Merge).
  * Include a link to the pull request in the issue.
* The core team looks at Pull Requests on a regular basis in a weekly triage
  meeting.
* After feedback has been given we expect responses within two weeks. After two
  weeks we may close the pull request if it isn't showing any activity.

# See also

* [Issue tracker](https://github.com/whosonfirst/whosonfirst-data/issues)
* [General GitHub documentation](http://help.github.com/)
* [GitHub pull request documentation](http://help.github.com/send-pull-requests/)
* [Long read about Who's On First](https://mapzen.com/blog/who-s-on-first/) - The introductory blog post, with pictures
* [Who's On First Comedy Skit](https://en.wikipedia.org/wiki/Who's_on_First%3F) - Background on the project name from Wikipedia

## See also-er

* [whosonfirst-names](https://github.com/whosonfirst/whosonfirst-names)
* [whosonfirst-dates](https://github.com/whosonfirst/whosonfirst-dates)
* [whosonfirst-placetypes](https://github.com/whosonfirst/whosonfirst-placetypes)
* [whosonfirst-sources](https://github.com/whosonfirst/whosonfirst-sources)
* [whosonfirst-tools](https://github.com/whosonfirst/whosonfirst-tools)
* [git-whosonfirst-data](https://github.com/whosonfirst/git-whosonfirst-data)

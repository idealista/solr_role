# Change Log
All notable changes to this project will be documented in this file.

## [Unreleased](https://github.com/idealista/solr_role/tree/develop)
### Fixed
- *[#68] Wrong user creation* @denics

## [3.2.0](https://github.com/idealista/solr_role/tree/3.2.0) (2024-03-25)
### Added
- *[#171](https://github.com/idealista/solr_role/issues/171) Add S3 backup for solr* @santi-eidu

## [3.1.3](https://github.com/idealista/solr_role/tree/3.1.3) (2023-01-26)
### Added
- *[#167](https://github.com/idealista/solr_role/issues/167) Add service template variable* @santi-eidu

## [3.1.2](https://github.com/idealista/solr_role/tree/3.1.2) (2023-01-17)
### Fixed
- *[#164](https://github.com/idealista/solr_role/issues/164) Reinstalling/Updating problem* @sorobon

## [3.1.1](https://github.com/idealista/solr_role/tree/3.1.1) (2022-11-07)
### Added
- *[#136](https://github.com/idealista/solr_role/issues/136) Add documentation about setting up cores and collections* @sorobon
### Fixed
- *[#160](https://github.com/idealista/solr_role/issues/160) Several errors in service template* @sorobon

## [3.1.0](https://github.com/idealista/solr_role/tree/3.1.0) (2022-09-07)
### Added
- *[#157](https://github.com/idealista/solr_role/issues/157) Add OS tunning* @MarioNv91 && @aren-pulid0

## [3.0.4](https://github.com/idealista/solr_role/tree/3.0.3) (2022-06-13)
### Fixed
- *[#154](https://github.com/idealista/solr_role/issues/154) fix task with tag solr_collections running on all hosts when the play set the batch size with serial 1* @ajiang

## [3.0.3](https://github.com/idealista/solr_role/tree/3.0.3) (2022-01-26)
### Added
- *[#149] Use provided configured value for `autoAddReplicas` at `Modify existing collections` step* @ilorancab

## [3.0.2](https://github.com/idealista/solr_role/tree/3.0.2) (2021-12-20)
### Added
- *[#141] Upgrade to version 8.11.0* @aren-pulid0
- *[#141] Fix log4j vulnerability* @aren-pulid0
- *[#141] Support for Debian 11 bullseye* @aren-pulid0

## [3.0.1](https://github.com/idealista/solr_role/tree/3.0.1) (2021-09-13)
### Changed
- *Default version as 8.9.0* @sorobon
### Fixed
- *[#137] Testing with debian buster failing* @sorobon

## [3.0.0](https://github.com/idealista/solr_role/tree/3.0.0) (2021-03-17)
### Added
- *[#127] Solr standalone mode support* @sorobon
### Changed
- *Role renamed to solr_role* @sorobon
- *Default version as 8.8.1*

## [2.5.1](https://github.com/idealista/solr_role/tree/2.5.1) (2020-08-10)
### Fixed
- *[#123] Notify when external libs added* @sorobon

## [2.5.0](https://github.com/idealista/solr_role/tree/2.5.0) (2020-06-02)
### Added
- *[#112](https://github.com/idealista/solr_role/issues/112) Support for package management* @sorobon

## [2.4.1](https://github.com/idealista/solr_role/tree/2.4.1) (2020-05-25)
### Changed
- *[#107](https://github.com/idealista/solr_role/issues/107) Default naven repository using https instead of http*  @sorobon
- *Bump ansible version to 2.8.8* @sorobon
- *[#110](https://github.com/idealista/solr_role/issues/110) Role fully compatible with solr 8.5.1* @sorobon
- *[#109](https://github.com/idealista/solr_role/issues/109) Migration to molecule 3.x* @sorobon
- *[#113](https://github.com/idealista/solr_role/issues/113) Rename role to solr_role* @sorobon
- *[#112](https://github.com/idealista/solr_role/issues/112) Improve agents management* @sorobon
- *[#117](https://github.com/idealista/solr_role/issues/117) Support for debian buster* @sorobon
### Fixed
- *[#106](https://github.com/idealista/solr_role/issues/106) Extra space in SOLR_ULIMIT_CHECKS var in solr.in.sh.j2*  @sorobon
### Removed
- *Only one molecule test with all options*  @sorobon

## [2.4.0](https://github.com/idealista/solr_role/tree/2.4.0) (2019-11-20)
### Added
- *[#100] JVM agents support* @sorobon
### Changed
- *[#98] Add template support for collections* @sorobon
- *[#98] Default version installed is Solr 8.3.0* @sorobon
- *[#100] Goss version used (0.3.7)* @sorobon
### Removed
- *[#98] Collection templates transfer using rsync module (no option available now)*

## [2.3.0](https://github.com/idealista/solr_role/tree/2.3.0) (2019-10-31)
### Changed
- *[#94] Upgrade to solr 8.2.0* @sorobon

## [2.2.0](https://github.com/idealista/solr_role/tree/2.2.0) (2019-06-19)
### Added
- *[#80](https://github.com/idealista/solr_role/issues/80) External libs support added* @sorobon
- *[#82](https://github.com/idealista/solr_role/issues/82) Java 11 support* @sorobon
- *Add ability to provide custom templates via `solr_templates_dir` variable* @jnogol

### Changed
- *[#88](https://github.com/idealista/solr_role/issues/88) Change "action" tasks to use uri module instead* @jnogol
- *[#87](https://github.com/idealista/solr_role/issues/87) Default version installed is Solr 8.1.1* @jnogol
- *Upgrade Ansible version to 2.5.15 in test-requirements to avoid CVE-2019-3828* @jnogol

### Fixed
- *[#90](https://github.com/idealista/solr_role/issues/90) Fix collection templates transfer adding copy module option* @jnogol

## [2.1.2](https://github.com/idealista/solr_role/tree/2.1.2) (2019-01-30)
### Changed
- *[#72](https://github.com/idealista/solr_role/issues/72) Adding cache and retries in remote package installation* @dortegau
### Fixed
- *[#75](https://github.com/idealista/solr_role/issues/75) Logging is not working* @sorobon

## [2.1.1](https://github.com/idealista/solr_role/tree/2.1.1) (2019-01-21)
[Full Changelog](https://github.com/idealista/solr_role/compare/2.1.0...2.1.1)
### Fixed
- *[#67](https://github.com/idealista/solr_role/issues/67) Role fails when collections aren't provided* @sorobon

## [2.1.0](https://github.com/idealista/solr_role/tree/2.1.0) (2018-12-19)
[Full Changelog](https://github.com/idealista/solr_role/compare/2.0.0...2.1.0)
### Changed
- *[#63](https://github.com/idealista/solr_role/issues/63) Installing Apache Solr 7.6.0 by default* @dortegau

## [2.0.0](https://github.com/idealista/solr_role/tree/2.0.0) (2018-12-17)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.9.0...2.0.0)
### Added
- *[#53](https://github.com/idealista/solr_role/issues/53) Adding tasks to manage collections* @dortegau

### Changed
- *[#58](https://github.com/idealista/solr_role/issues/58) Testing against a cluster with two nodes (solrcloud1 and solrcloud2) instead of one* @dortegau
- *[#54](https://github.com/idealista/solr_role/issues/54) Installing SolrCloud 7.5.0 by default* @dortegau
- *[#55](https://github.com/idealista/solr_role/issues/55) Upgrading Java and ZooKeeper roles to latest versions, using hostmanager plugin to manage network instead of landrush, adding test-requirements.txt for execution under pipenv and upgrading to Ansible 2.5.5.0* @dortegau

## [1.9.0](https://github.com/idealista/solr_role/tree/1.9.0) (2018-02-12)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.8.0...1.9.0)
### Changed
- *[#47](https://github.com/idealista/solr_role/issues/47) Configure zookeeper client timeout* @danieljesus
- *[#14](https://github.com/idealista/solr_role/issues/14) Add Travis CI* @jnogol

## [1.8.0](https://github.com/idealista/solr_role/tree/1.8.0) (2017-09-26)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.7.0...1.8.0)

### Fixed
- *[#43](https://github.com/idealista/solr_role/issues/43) Forcing XML response in admin/info request handler due to change to JSON as default response format* @dortegau

### Changed
- *[#41](https://github.com/idealista/solr_role/issues/41) Upgrading to SolrCloud 7.0.0* @dortegau

## [1.7.0](https://github.com/idealista/solr_role/tree/1.7.0) (2017-06-29)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.6.0...1.7.0)

### Changed
- *[#36](https://github.com/idealista/solr_role/issues/36) Support Debian stretch* @jmonterrubio


## [1.6.0](https://github.com/idealista/solr_role/tree/1.6.0) (2017-04-24)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.5.2...1.6.0)

### Changed
- *[#30](https://github.com/idealista/solr_role/issues/30) Upgrading to SolrCloud 6.5.0* @dortegau

### Fixed
- *[#26](https://github.com/idealista/solr_role/issues/26) Fixing configuration issues in tests when default TLD was added* @dortegau


## [1.5.2](https://github.com/idealista/solr_role/tree/1.5.2) (2017-04-21)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.5.1...1.5.2)

### Fixed
- *[#24](https://github.com/idealista/solr_role/issues/24) Fixing jetty-xml configuration file (deleting values inside config sets)* @dortegau
- *[#26](https://github.com/idealista/solr_role/issues/26) Adding default TLD in molecule.yml* @dortegau

## [1.5.1](https://github.com/idealista/solr_role/tree/1.5.1) (2017-04-21)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.5.0...1.5.1)

### Fixed
- *[#21](https://github.com/idealista/solr_role/issues/21) Fixing Acceptor/Selector thread configuration in jetty-http template* @dortegau

## [1.5.0](https://github.com/idealista/solr_role/tree/1.5.0) (2017-03-31)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.4.0...1.5.0)

### Added
*Renamed some vars (backwards compatible!)* @jmonterrubio

### Fixed
- *[#18](https://github.com/idealista/solr_role/issues/18) Check version for conditional installation* @jmonterrubio

## [1.4.0](https://github.com/idealista/solr_role/tree/1.4.0) (2017-03-16)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.3.0...1.4.0)

### Added
- *[#15](https://github.com/idealista/solr_role/issues/15) Add jetty-http config file* @javierRobledo

## [1.3.0](https://github.com/idealista/solr_role/tree/1.3.0) (2017-02-23)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.2.0...1.3.0)

### Added
- *[#11](https://github.com/idealista/solr_role/issues/11) Add mount folder for backup* @jmonterrubio

## [1.2.0](https://github.com/idealista/solr_role/tree/1.2.0) (2017-01-27)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.1.1...1.2.0)

### Added
- *[#8](https://github.com/idealista/solr_role/issues/8) Set JVM args by configuration* @jmonterrubio

## [1.1.1](https://github.com/idealista/solr_role/tree/1.1.1) (2017-01-11)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.1.0...1.1.1)

### Fixed
- *[#4](https://github.com/idealista/solr_role/issues/4) Copy solr.xml file for not default data dir* @jmonterrubio

## [1.1.0](https://github.com/idealista/solr_role/tree/1.1.0)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.0.1...1.1.0)

### Added
- *[#1](https://github.com/idealista/solr_role/issues/1) Enable all the jetty HttpConfiguration parameters from ansible* @jmonterrubio

### Fixed
- *Renamed solr_role in tests playbook* @jmonterrubio

## [1.0.1](https://github.com/idealista/solr_role/tree/1.0.1)
[Full Changelog](https://github.com/idealista/solr_role/compare/1.0.0...1.0.1)

### Fixed
- *JMX enable* @jmonterrubio

### Added
- *Log configuration* @jmonterrubio
- *Update doc* @jmonterrubio
- *Code refactor* @jmonterrubio
- *Update SolrCloud sources repository* @jmonterrubio

## [1.0.0](https://github.com/idealista/solr_role/tree/1.0.0)
### Added
- *First commit* @jmonterrubio

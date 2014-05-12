![Image](http://genomicsandhealth.org/files/logo_ga.png)


# Schemas for the Global Alliance Data Working Group


The [Global Alliance for Genomics and Health][ga4gh] is an international
coalition, formed to enable the sharing of genomic and clinical data.

The [Data Working Group](http://genomicsandhealth.org/files/public/Priorities%20-%20without%20membership%20DWG_0.pdf) concentrates on data representation, storage, and analysis, including working with platform development partners and industry leaders to develop standards that will facilitate interoperability.

Each area of genomics and health has a dedicated team working to define those standards.


## Reads Task Team

The [Reads Task Team](https://groups.google.com/forum/#!forum/dwgreadtaskteam) is focused on standards for accessing genomic read data -- collections of primary data collected from sequencing machines.

The team will deliver:
  1. Data model. An abstract, mathematically complete and precise model of the data that is manipulated by the API.
  2. API Specification. A human-readable document introducing and defining the API, accompanied by a formal specification.
  3. Reference Implementation. Open source working code demonstrating the API, ideally which can underpin real world working implementations.


## File Formats Task Team

One small but essential part of this effort is the definition,
standardisation, and improvement of basic file formats for sequence and
variation data, and for associated infrastructure such as index formats.

These format specifications can be found in the
[samtools/hts-specs repository][hts-specs].

[ga4gh]:      http://genomicsandhealth.org/
[hts-specs]:  https://github.com/samtools/hts-specs


## Build Status

[![Build Status](https://travis-ci.org/ga4gh/ReadTaskTeam.svg?branch=master)](https://travis-ci.org/ga4gh/ReadTaskTeam)

## How to contribute changes

See the [CONTRIBUTING.md](CONTRIBUTING.md) documement.

## License

See the [LICENSE](LICENSE)

#!/usr/bin/env python

import string

def fixNone(s):		# convert python None to a printable string
    if s == None:
	return ""
    else:
	return s

# Mostly generated code from MouseMine...

# This is an automatically generated script to run your query
# to use it you will require the intermine python client.
# To install the client, run the following command from a terminal:
#
#     sudo easy_install intermine
#
# For further documentation you can visit:
#     http://www.intermine.org/wiki/PythonClient

# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("http://www.mousemine.org/mousemine/service")

# Get a new query on the class (table) you will be querying:
query = service.new_query("OntologyTerm")

# Type constraints should come early - before all mentions of the paths they constrain
query.add_constraint("ontologyAnnotations.subject", "Genotype")

# The view specifies the output columns
query.add_view(
    "identifier", "name", "namespace",
    "ontologyAnnotations.subject.primaryIdentifier",
    "ontologyAnnotations.subject.name", "ontologyAnnotations.qualifier",
    "ontologyAnnotations.evidence.code.code",
    "ontologyAnnotations.evidence.publications.mgiJnum"
)

# Uncomment and edit the line below (the default) to select a custom sort order:
# query.add_sort_order("OntologyTerm.identifier", "ASC")

# You can edit the constraint values below
query.add_constraint("ontologyAnnotations.ontologyTerm.ontology.name", "=", "Mammalian Phenotype", code = "A")

# Uncomment and edit the code below to specify your own custom logic:
# query.set_logic("A")

# This output code was not generated by MouseMine
# just writing tab delimited output with a header line and handling
#  possible None values for qualifier
print string.join(["term identifier", "term", "namespace", "object identifier",
	"object name", "qualifier", "evidence code", "reference"], sep='\t')
for row in query.rows():
    print string.join([row["identifier"], row["name"], row["namespace"], \
        row["ontologyAnnotations.subject.primaryIdentifier"], \
        row["ontologyAnnotations.subject.name"],
	fixNone( row["ontologyAnnotations.qualifier"]), \
        row["ontologyAnnotations.evidence.code.code"], \
        row["ontologyAnnotations.evidence.publications.mgiJnum"]], sep='\t')

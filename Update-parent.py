# Update-parent.py
# (c) David Waelder 2016 - 2017
#
# This script takes the value of the Original Estimate field of the subtask
# and copies it to a custom field in its parent issue.

# CustomFieldManager enables access to the Custom Fields objects, that is global object.
from com.atlassian.jira.issue import CustomFieldManager

# my_customField gets the desired custom field (customfield_12731) object.
my_customField = customFieldManager.getCustomFieldObject(12731)

# We get the Original Estimate value (in seconds) and convert it into hours (two decimals).
the_estimation = round(issue.getOriginalEstimate()/3600,2)
the_hours = str(the_estimation) + " h"

# We get into my_parent the parent issue of the current subtask.
my_parent = issue.getParentObject()

# Using the updateValue function from the CustomFieldType, we update the parent
# custom field value.
my_customField.getCustomFieldType().updateValue(my_customField,my_parent,the_hours)

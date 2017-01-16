# Update-parent.py
# (c) David Waelder 2016 - 2017
#
# This script takes the value of the Original Estimate field of the subtask
# and copies it to a custom field in its parent issue.

from com.atlassian.jira.component import ComponentAccessor      # ComponentAccessor enables access to the Custom Fields objects, that is global
from com.atlassian.jira.issue import CustomFieldManager         # 
from com.atlassian.jira.issue.fields import CustomField

customField = customFieldManager.getCustomFieldObject(12731)

estimation = round(issue.getOriginalEstimate()/3600,2)
thehours = str(estimation) + " h"

issue.setDescription(str(estimation))

parent = issue.getParentObject()

customField.getCustomFieldType().updateValue(customField,parent,thehours)

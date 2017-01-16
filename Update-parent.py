from com.atlassian.jira.component import ComponentAccessor
from com.atlassian.jira.issue import CustomFieldManager
from com.atlassian.jira.issue.fields import CustomField

customFieldManager = ComponentAccessor.getCustomFieldManager()
customField = customFieldManager.getCustomFieldObject(12731)

estimation = round(issue.getOriginalEstimate()/3600,2)
thehours = str(estimation) + " h"

issue.setDescription(str(estimation))

parent = issue.getParentObject()

customField.getCustomFieldType().updateValue(customField,parent,thehours)

# Create_subtasks.py
# (c) David Waelder 2017
#
# This script creates substasks on a given issue once a transition executed.

# Import global objects needed to access the data.
from com.atlassian.jira.util import ImportUtils
from com.atlassian.jira import ManagerFactory

#my_issue = issue.getKey()

#issue.setDescription(my_issue)

my_issueManager = ComponentManager.getInstance().getIssueManager()
my_issueFactory = ComponentManager.getInstance().getIssueFactory()
my_authenticationContext = ComponentManager.getInstance().getJiraAuthenticationContext()
my_subTaskManager = ComponentManager.getInstance().getSubTaskManager()

#
# Prepare the issue object that we will use to create the subtask
#
my_issueObject = my_issueFactory.getIssue()
# Set project based on parent issue
my_issueObject.setProject(issue.getProject())
# Set issue type to the IT Assessment substask
my_issueObject.setIssueTypeId("11206")
# Set parent ID of the subtask we are creating
my_issueObject.setParentId(issue.getId())
my_summary = issue.getSummary() + " - IT Assessment"
my_issueObject.setSummary(my_summary)

#
# Create the subtask
#
my_subTask = issueManager.createIssue(authenticationContext.getUser(), my_issueObject)
subTaskManager.createSubTaskIssueLink(issue.getGenericValue(), my_subTask, authenticationContext.getUser())

# Update search indexes
ImportUtils.setIndexIssues(True);
ManagerFactory.getCacheManager().flush(CacheManager.ISSUE_CACHE,my_subTask)
ComponentManager.getInstance().getIndexManager().reIndex(my_subTask)
ImportUtils.setIndexIssues(False)

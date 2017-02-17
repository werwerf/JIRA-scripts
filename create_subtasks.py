# Create_subtasks.py
# (c) David Waelder 2017
#
# This script creates substasks on a given issue once a transition executed.

# Import global objects needed to access the data and objects.
from com.atlassian.jira.util import ImportUtils
from com.atlassian.jira import ManagerFactory
from com.atlassian.jira.component import ComponentAccessor


# IssueManager gives us access to the method to create the issue
my_issueManager = ComponentAccessor.getIssueManager()
# IssueFactory enables us to create the blank issue and set the values
my_issueFactory = ComponentAccessor.getIssueFactory()
# We need the Authentication context to pass the user creating the subtask
my_authenticationContext = ComponentAccessor.getJiraAuthenticationContext()
# SubtaskManager enables us to create the link with the parent task
my_subTaskManager = ComponentAccessor.getSubTaskManager()

# We check if the task has already subtasks
if issue.getSubTaskObjects().isEmpty():
	#
	# Prepare the issue object that we will use to create the subtask
	#
	# We create the blank issue object
	my_issueObject = my_issueFactory.getIssue()
	# Set project based on parent issue
	my_issueObject.setProject(issue.getProject())
	# Set issue type to the IT Assessment substask
	my_issueObject.setIssueTypeId("11206")
	# Set parent ID of the subtask we are creating
	my_issueObject.setParentId(issue.getId())
	# Get the summary from the parent issue and modify it for the subtask
	my_summary = issue.getSummary() + " - IT Assessment"
	my_issueObject.setSummary(my_summary)
	#
	# Create the subtask
	#
	# Create the issue
	my_subTask = my_issueManager.createIssueObject(my_authenticationContext.getLoggedInUser(), my_issueObject)
	# Create the task - Subtask link
	my_subTaskManager.createSubTaskIssueLink(issue, my_subTask, my_authenticationContext.getLoggedInUser())

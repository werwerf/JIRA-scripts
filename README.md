# JIRA-scripts

Set of scripts in jython created for JIRA automation tasks. The scripts are to be executed during transitions post action using the JIRA Scripting Suite add-on (https://quisapps.com/confluence/pages/viewpage.action?pageId=8978487)

Scripts list

- Update_parent: executed in a transition, gets the original estimation of the subtask and updates a custom field in the parent 
  task with the value of the original estimation.

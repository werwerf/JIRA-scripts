<!-- @@Formula:

Iterator grps = issue.get("customfield_12406").iterator();
String grpsStr = "";

while (grps.hasNext()){
   grpsStr = grpsStr + "\"" + grps.next().getName() + "\",";
}
grpsStr = grpsStr + "\"confluence-users\"";

return "{ \"name\" : \"" + issue.get("customfield_12407") + "\", \"groups\" :[ " + grpsStr + "],\"active\" : true,\"email\" : \"" + issue.get("customfield_12408") + "\",\"fullname\" : \"" + issue.get("customfield_12403") + "\"},";

-->

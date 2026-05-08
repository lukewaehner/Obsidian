---
tags:
  - <% tp.file.cursor(1) %>
type: moc
---
<%* const id = crypto.randomUUID(); -%>

```folder-overview
id: <% id %>
folderPath: <% tp.file.folder(true) %>
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="<% id %>"></span>
<span class="fv-link-list-end" id="<% id %>"></span>


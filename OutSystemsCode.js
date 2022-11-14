// Server Actions

// CREATE
Controller.prototype.createClientAction$ServerAction = function (clientDataIn, callContext) {
var controller = this.controller;
var inputs = {
ClientData: OS.DataConversion.ServerDataConverter.to(clientDataIn, OS.Types.Record)
};
return controller.callServerAction("CreateClientAction", "screenservices/UI/MainFlow/Screen1/ActionCreateClientAction", "ZuNZsf8bVaO2FKNEU_XfKw", inputs, controller.callContext(callContext), OutSystemsDebugger.getRequestHeaders(callContext.id), function (json, headers) {
OutSystemsDebugger.processResponseHeaders(callContext.id, headers);
}, false).then(function (outputs) {
});
};


// READ
Controller.prototype.readClientAction$ServerAction = function (clientIdIn, callContext) {
var controller = this.controller;
var inputs = {
ClientId: OS.DataConversion.ServerDataConverter.to(clientIdIn, OS.Types.LongInteger)
};
return controller.callServerAction("ReadClientAction", "screenservices/UI/MainFlow/Screen1/ActionReadClientAction", "MCleeaZEqgPSbIrWMXcYWw", inputs, controller.callContext(callContext), OutSystemsDebugger.getRequestHeaders(callContext.id), function (json, headers) {
OutSystemsDebugger.processResponseHeaders(callContext.id, headers);
}, false).then(function (outputs) {
});
};


// UPDATE
Controller.prototype.updateClientAction$ServerAction = function (clientDataIn, callContext) {
var controller = this.controller;
var inputs = {
ClientData: OS.DataConversion.ServerDataConverter.to(clientDataIn, OS.Types.Record)
};
return controller.callServerAction("UpdateClientAction", "screenservices/UI/MainFlow/Screen1/ActionUpdateClientAction", "clV_iHZKzuJZGkbqiTtUeg", inputs, controller.callContext(callContext), OutSystemsDebugger.getRequestHeaders(callContext.id), function (json, headers) {
OutSystemsDebugger.processResponseHeaders(callContext.id, headers);
}, false).then(function (outputs) {
});
};


// DELETE
Controller.prototype.deleteClientAction$ServerAction = function (clientIdIn, callContext) {
var controller = this.controller;
var inputs = {
ClientId: OS.DataConversion.ServerDataConverter.to(clientIdIn, OS.Types.LongInteger)
};
return controller.callServerAction("DeleteClientAction", "screenservices/UI/MainFlow/Screen1/ActionDeleteClientAction", "msIHpY_2Yykmt5+glEArdg", inputs, controller.callContext(callContext), OutSystemsDebugger.getRequestHeaders(callContext.id), function (json, headers) {
OutSystemsDebugger.processResponseHeaders(callContext.id, headers);
}, false).then(function (outputs) {
});
};



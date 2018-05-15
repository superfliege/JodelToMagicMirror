
Module.register("self-jodelapi",{
// Default module config.
	


defaults: {
	text: "Hello World!",
	updateInterval: 4000,
	animatedSpeed: 0,
	},

start: function() {
	this.jodelapicontent = "fetching";
	this.sendSocketNotification("CONFIGJODEL", this.config)
},

socketNotificationReceived: function(notification, payload) {
	if (notification === 'JODELAPI') {
	this.jodelapicontent = payload;
	this.updateDom();
	}
},
getDom: function() {
	var wrapper = document.createElement("div");
	wrapper.innerHTML = this.jodelapicontent;
	return wrapper;
	}
});


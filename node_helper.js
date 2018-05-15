var NodeHelper = require("node_helper");
var sys = require('sys');
var exec = require('child_process').exec;


module.exports = NodeHelper.create({
	start: function() {
		console.log("Starting node helper: " + this.name);
	},

	// Subclass socketNotificationReceived received.
	socketNotificationReceived: function(notification, payload) {
		var self = this;
		if (notification === 'CONFIGJODEL') {

			this.config = payload;
			setInterval(function() {
				self.sendJodel();
			}, this.config.updateInterval);
		}
		
	},

	sendJodel: function() {
		var self = this;
		child = exec("cat /home/pi/MagicMirror/modules/self-jodelapi/jodelexport.html", function (error, stdout, stderr) {
			if (error) {
				console.log(error);
				return;
			}
		self.sendSocketNotification('JODELAPI', stdout);
		});
	}
});

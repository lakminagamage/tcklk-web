const mediaQuery = window.matchMedia('(max-width: 768px)');
 
function handleTabletChange(e) {
  
if (e.matches) {


tsParticles.load("tsparticles", {
particles: {
	number: {
		value: 50
	},
	color: {
		value: "#ffffff",
		animation: {
			enable: true,
			speed: 50,
			sync: false
		}
	},
	shape: {
		type: "circle",
	},
	size: {
		value: 3,
		random: true,
		animation: {
			enable: true,
			speed: 16,
			minimumValue: 0.1,
			sync: false
		}
	},
	links: {
		enable: true,
		distance: 200,
		color: "random",
		opacity: 0.4,
		width: 1
	},
	move: {
		enable: true,
	},
},
interactivity: {
	detectsOn: "canvas",
	events: {
		onHover: {
			enable: false,
			mode: "repulse"
		},
		onClick: {
			enable: false,
			mode: "bubble"
		},
		resize: true
	},
	modes: {
		grab: {
			distance: 100,
			links: {
				opacity: 1
			}
		},
		bubble: {
			distance: 400,
			size: 40,
			duration: 2,
			opacity: 0.8
		},
		repulse: {
			distance: 100
		},
		push: {
			quantity: 4
		},
		remove: {
			quantity: 2
		}
	}
},
detectRetina: true,
});


}
else{

tsParticles.load("tsparticles", {
particles: {
	number: {
		value: 70
	},
	color: {
		value: "#ffffff",
		animation: {
			enable: true,
			speed: 50,
			sync: false
		}
	},
	shape: {
		type: "circle",

	},
	size: {
		value: 3,
		random: true,
		animation: {
			enable: true,
			speed: 16,
			minimumValue: 0.1,
			sync: false
		}
	},
	links: {
		enable: true,
		distance: 200,
		color: "random",
		opacity: 0.5,
		width: 1
	},
	move: {
		enable: true,
	},
},
interactivity: {
	detectsOn: "canvas",
	events: {
		onHover: {
			enable: true,
			mode: "repulse"
		},
		onClick: {
			enable: false,
			mode: "bubble"
		},
		resize: true
	},
	modes: {
		grab: {
			distance: 100,
			links: {
				opacity: 1
			}
		},
		bubble: {
			distance: 400,
			size: 40,
			duration: 2,
			opacity: 0.8
		},
		repulse: {
			distance: 100
		},
		push: {
			quantity: 4
		},
		remove: {
			quantity: 2
		}
	}
},
detectRetina: true,
});



}
}
 

mediaQuery.addListener(handleTabletChange);


handleTabletChange(mediaQuery);
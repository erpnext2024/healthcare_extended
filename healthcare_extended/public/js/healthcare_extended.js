//Popup Functionality
document.addEventListener('DOMContentLoaded', function () {
	var popup_toggle_buttons = document.querySelectorAll('.nexusuite-toggle-popup');

	popup_toggle_buttons.forEach(function (button) {
		button.addEventListener('click', function () {
			var popupId = this.getAttribute('data-popup-id');
			var popup = document.getElementById(popupId);

			if (popup)
				popup.style.display = 'flex';
		});
	});

	var popup_close_buttons = document.querySelectorAll('.nexusuite-popup-close');

	popup_close_buttons.forEach(function (closeButton) {
		closeButton.addEventListener('click', function () {

			var popupWrapper = this.closest('.nexusuite-popup-wrapper');
			if (popupWrapper)
				popupWrapper.style.display = 'none';

		});
	});
});

//Section Break Frontend Functionality


document.addEventListener('DOMContentLoaded', function () {
	function getElementsBetween(startElement, stopClass) {
		let elements = [];
		let currentElement = startElement.nextElementSibling;

		while (currentElement && !currentElement.classList.contains(stopClass)) {
			console.log(currentElement.classList);

			elements.push(currentElement);
			currentElement = currentElement.nextElementSibling;
		}

		return elements;
	}

	document.querySelectorAll(".nexusuite-input-section-break:not(:first-child)").forEach(function (sectionBreak) {
		let elements = getElementsBetween(sectionBreak, 'nexusuite-input-section-break'); // Replace 'stop-class' with your specific class

		elements.forEach(function (element) {
			element.setAttribute('data-parent', sectionBreak.getAttribute('id'));
		});

		sectionBreak.addEventListener('click', function () {
			let isHidden = this.classList.contains('hidden-section-break');
			let sectionBreakElement = this;

			let elements = document.querySelectorAll(`[data-parent='${this.getAttribute('id')}']`);
			elements.forEach(function (element) {
				if (isHidden) {
					element.style.display = "";
					sectionBreakElement.classList.remove('hidden-section-break');
				} else {
					element.style.display = "none";
					sectionBreakElement.classList.add('hidden-section-break');
				}
			});
		});
	});
});

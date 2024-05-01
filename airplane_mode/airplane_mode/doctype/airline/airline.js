// Copyright (c) 2024, Lay Virak and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });

// add btn view website
frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Fetch the value of the website field
        var website = frm.doc.website;
        
        // Check if the website field has a value
        if (website) {
            // Create a link to the website
            var link = '<div class="website-link"><a href="' + website + '" target="_blank">Visit Website</a></div>';
            
            // Append the link to the sidebar
            // frm.sidebar.add_user_action("Visit Website", function() {
            //     window.open(website, '_blank');
            // });
            frm.add_web_link('link', link, false, 'Visit Website');
        }
    }
});



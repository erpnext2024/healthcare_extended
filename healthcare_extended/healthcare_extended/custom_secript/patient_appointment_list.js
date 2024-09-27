frappe.listview_settings['Patient Appointment'] = {
    refresh: function(listview) {
         const map = {
            "Scheduled":{"background-color":"#0172CB", "color":"white"},
            "Open":{"background-color":"#00A58E", "color":"white"},
            "Checked In":{"background-color":"#D26843", "color":"white"},
            "Checked Out":{"background-color":"red", "color":"white"},
            "Closed":{"background-color":"#F3BE07", "color":"white"},
            "Cancelled":{"background-color":"#D21C1C", "color":"white"},
            "No Show":{"background-color":"#F4F4F5", "color":"white"}
        };
        Object.keys(map).forEach((key)=>{
            listview.$result.find('[data-filter="status,=,'+key+'"]').css(map[key]);
        })
    }
};
frappe.listview_settings['Healthcare Practitioner'] = {
    refresh: function(listview) {
         const map = {
            "Active":{"background-color":"#00A58E", "color":"white"},
            "Inactive":{"background-color":"grey", "color":"white"},
        };
        Object.keys(map).forEach((key)=>{
            listview.$result.find('[data-filter="status,=,'+key+'"]').css(map[key]);
        })
    }
};
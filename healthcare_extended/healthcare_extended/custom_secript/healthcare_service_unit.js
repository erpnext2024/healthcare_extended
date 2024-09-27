frappe.listview_settings['Healthcare Service Unit'] = {
    onload: function(listview) {
        // Your custom code here, if needed
    },

    refresh: function(listview) {
         const map = {
        "Enabled": "#9370DF"
        };
        Object.keys(map).forEach((key)=>{
            listview.$result.find('[data-filter="project__overall_project_status,=,'+key+'"]').removeClass('gray').addClass(map[key]);
        })
    }
};
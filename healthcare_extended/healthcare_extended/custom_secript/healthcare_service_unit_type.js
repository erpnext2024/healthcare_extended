frappe.listview_settings['Healthcare Service Unit Type'] = {
    refresh: function(listview) {
         const map = {
            "0":{"background-color":"#7F56D9", "color":"white"},
            "1":{"background-color":"grey", "color":"white"},
        };
        Object.keys(map).forEach((key)=>{
            listview.$result.find('[data-filter="disabled,=,'+key+'"]').css(map[key]);
        })
    }
};
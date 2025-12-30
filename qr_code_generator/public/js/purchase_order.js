
frappe.ui.form.on('Purchase Order', {
    refresh(frm) {
        frappe.call({
            method: 'qr_code_generator.api.qr_code.gen_qr', // backend method
            args: {
                data: frm.doc.name
            },
            callback: function(r) {
                if (r.message) {
                    const qr_html = `${r.message}`;
                    frm.fields_dict.custom_qr_code.$wrapper.html(qr_html);
                }
            }
        });
    }
});

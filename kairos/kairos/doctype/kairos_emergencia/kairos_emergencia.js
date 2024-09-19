// Copyright (c) 2024, AEI and contributors
// For license information, please see license.txt

frappe.ui.form.on("kairos_emergencia", {
	department(frm) {
        frm.set_query('employee', () => {
            return {
                filters: {
                    department: frm.doc.department
                }
            }
        })

	},
    agregar_movimiento: function(frm) {
        frm.add_child('detalle_movimiento', {
            "id_emergencia": frm.doc.name,
            "department": frm.doc.department,
            "employee": frm.doc.employee,
            "nota": frm.doc.nota});
        frm.refresh_field('detalle_movimiento');
    }
    
    

});

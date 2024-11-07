// Copyright (c) 2024, AEI and contributors
// For license information, please see license.txt

frappe.ui.form.on("kairos_expediente", {
        onload(frm){
                frm.set_query('employee', () => {
                        return {
                                filters: {
                                        department: frm.doc.department
                                }
                        }
                        })
        }
	// timeline_refresh(frm) {
        //         let track=cur_frm.timeline.timeline_items
        //         let value;
        //         frm.doc.tracking = []
        //         if(track){
        //                 for (let i of track){
        //                         value = i;
        //                         const input = value.content;
        //                         if(input.includes("assigned")){

        //                                 const parts = input.split(" assigned ");
        //                                 const part1 = parts[0].trim();

        //                                 const restParts = parts[1].split(": ");
        //                                 const part2 = restParts[0].trim();
        //                                 const part3 = restParts[1].trim();
        //                                 const datetime = value.creation;

        //                                 const datetimeWithoutMilliseconds = datetime.split('.')[0];
        //                                 frm.add_child('tracking', {
                                        
        //                                         creation1:datetimeWithoutMilliseconds,
        //                                         assigned_by:part1,
        //                                         assigned_to:part2,
        //                                         comment : part3
        //                                 });
        //                         }
        //                 }
        //         }
        //         frm.refresh_field('tracking');              
              
        // },
});

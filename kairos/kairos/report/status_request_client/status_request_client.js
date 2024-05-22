// Copyright (c) 2024, AEI and contributors
// For license information, please see license.txta
frappe.query_reports["Status Request Client"] = {
	"filters": [
		{
            fieldname: 'employee_name',
            label: __('Employee Name'),
			fieldtype: 'Link',
            options: 'Employee',
             
        },
        {
            fieldname: 'department_name',
            label: __('Department Name'),
			fieldtype: 'Link',
            options: 'Department',
		
           
        },
        {
            fieldname: 'finish_date',
            label: __('Finsh Date'),
			fieldtype: 'Date',
		
           
        },
	
		{
            fieldname: 'days_in_department',
            label: __('Days In Department'),
			fieldtype: 'Data',
        },
		
		{
            fieldname: 'status',
            label: __('Status'),
            fieldtype: 'Select',
            options:  [
                '',
                'Approved',
                'Rejected',
                'Completed',
                'Pending'
            ],
		
           
        },
	],
   
};
// Copyright (c) 2024, Lay Virak and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });


// frappe.ui.form.on(
//     "Airplane Ticket",
//     (cur_frm.fields_dict["add_ons"].grid.get_field("item").get_query = function (
//       doc
//     ) {
//       return {
//         filters: {
//           name: ["not in", doc.add_ons.map((i) => i?.item)],
//         },
//       };
//     })
//   );

// set value to seat
frappe.ui.form.on("Airplane Ticket", {
  refresh: function (frm) {
    frm.add_custom_button(
      "Select Seat",
      () => {
        frappe.prompt(
          [{ fieldname: "seat", fieldtype: "Data", label: "Seat Number" }],
          function (values) {
            frm.set_value("seat", values.seat);
          },
          "Enter Seat Number",
          "Set"
        );
      },
      "Action"
    );
  },
});
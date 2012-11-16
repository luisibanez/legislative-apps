/**
  *  Notes -  This function computes statistics on the number of differences between two bills.
  * 
  *  It is inspired in the behavior of the Git command
  *
  *                          git diff --stat
  * 
  **/

/*
 *  Getting two bills
 */
  function getBill() {
     var billId="S1234-2011"
	   var billURL = "http://open.nysenate.gov/legislation/2.0/bill/" + billId + ".jsonp";
     document.write(billURL);
     return billURL
     }


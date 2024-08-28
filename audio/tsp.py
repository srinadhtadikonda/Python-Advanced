!DOCTYPE html>
<html>

<body>
  <p>How would you like your coffee?</p>
  <form>
    <input type="checkbox" name="coffee" value="cream" onchange="updateOrder()">With cream<br>
    <input type="checkbox" name="coffee" value="sugar" onchange="updateOrder()">With sugar<br>
    <input type="text" id="order" size="50">
  </form>

  <script>
    function updateOrder() {
      // Get all checkboxes with the name "coffee"
      var checkboxes = document.getElementsByName('coffee');

      // Filter out the checked checkboxes
      var checkedCheckboxes = Array.from(checkboxes).filter(checkbox => checkbox.checked);

      // Check if any checkboxes are checked
      if (checkedCheckboxes.length > 0) {
        // Get the values of the checked checkboxes
        var selectedValues = checkedCheckboxes.map(checkbox => checkbox.value);

        // Update the text input with the selected values
        document.getElementById('order').value = "You ordered coffee with " + selectedValues.join(', ');
      } else {
        // No checkboxes are checked, set the text input to empty
        document.getElementById('order').value = "";
      }
    }
  </script>
</body>

</html>

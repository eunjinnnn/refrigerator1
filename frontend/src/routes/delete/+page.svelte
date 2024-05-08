<script>
  import { Input, Label, Helper, Button, Checkbox, A , Select} from 'flowbite-svelte';

  let cat_selected;
  let unit_selected;
  let volume;
  let foodname;
  
  let categories = [
        { value: 1, name: 'VEGETABLES' },
        { value: 2, name: 'DRINKS' },
        { value: 3, name: 'FROZEN FOOD' },
        { value: 4, name: 'ETC' }
    ];

  let units = [
        { value: 1, name: '개' },
        { value: 2, name: 'L' },
        { value: 3, name: '조각' }
    ];
</script>

<form>
  <div class="grid gap-6 mb-6 sm:grid-cols-3">
    <div>
      <Label for="purchaseDate" class="mb-2">Category</Label>
      <Select id="select-category" size="md" items={categories} placeholder="Category"/>
    </div>
    <div>
      <Label for="purchaseDate" class="mb-2">Foodname</Label>
      <Input type="text" id="foodname" placeholder="Foodname" required/>
    </div>
    <div>
      <Label for="purchaseDate" class="mb-2">Volume</Label>
      <Input type="number" id="volume" placeholder="Volume" required />
    </div>
    <div>
      <Label for="purchaseDate" class="mb-2">Unit</Label>
      <Select id="select-category" size="md" items={units} placeholder="Unit"/>
    </div>
    <div>
      <Label for="purchaseDate" class="mb-2">Purchase Date</Label>
      <Input type="date" id="purchaseDate" required />
    </div>
    <div>
      <Label for="expirationDate" class="mb-2">Expiration date</Label>
      <Input type="date" id="expirationDate" required />
    </div>
  </div>
  <div>

  </div>
  <Button type="submit">ADD</Button>
</form>
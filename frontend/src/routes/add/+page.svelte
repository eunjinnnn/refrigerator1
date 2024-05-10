<script>
  import { Input, Label, Helper, Button, Checkbox, A , Select, Card} from 'flowbite-svelte';

  let cat_selected = ['food1', 'food2'];
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

<form class = 'flex-1 w-20'>
    <div class="flex gap-6 mb-6">
        <div class = 'fiex w-30 h-16'>
            <Label for="purchaseDate" class="mb-2" style='font-size:x-small'>Category</Label>
            <Select id="select-category" class='fiex w-20' style='font-size:x-small' size="sm" items={categories} placeholder="Category"/>
        </div>
        <div class = 'fiex w-30 h-16'>
            <Label for="purchaseDate" class="mb-2" style='font-size:x-small'>Foodname</Label>
            <Input type="text" class='fiex w-20' id="foodname" style='font-size:x-small' placeholder="Foodname" required/>
        </div>
        <div class = 'fiex w-30 h-16'>
            <Label for="purchaseDate" class="mb-2" style='font-size:x-small'>Volume</Label>
            <Input type="number" class='fiex w-20' id="volume" style='font-size:x-small' placeholder="Volume" required />
        </div>
    </div>
    <div class="flex gap-6 mb-6">
        <div class = 'fiex w-30 h-16'>
            <Label for="purchaseDate" class="mb-2" style='font-size:x-small'>Unit</Label>
            <Select id="select-category" class='fiex w-20' size="md" style='font-size:x-small' items={units} placeholder="Unit"/>
        </div>
        <div class = 'fiex w-30 h-16'>
            <Label for="purchaseDate" class="mb-2" style='font-size:x-small'>Purchase Date</Label>
            <Input type="date" class='fiex w-20'  style='font-size:x-small' id="purchaseDate" required />
        </div>
        <div class = 'fiex w-30 h-16'>
            <Label for="expirationDate" class="mb-2" style='font-size:x-small'>Expiration date</Label>
            <Input type="date" class='fiex w-20' id="expirationDate" style='font-size:x-small' required />
        </div>
    </div>
    <Button type="submit" size = 'xs' style='font-size:x-small'>ADD</Button>
</form>

{#each cat_selected as cat}
    <Card class = 'flex-1 w-20'>
        <p>{cat}</p>
    </Card>
{/each}

<Button type='submit' size = 'xs'> OK </Button>
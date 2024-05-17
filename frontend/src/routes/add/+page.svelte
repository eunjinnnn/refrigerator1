<script>
  import { Input, Label, Helper, Button, Checkbox, A , Select, Card} from 'flowbite-svelte';

  let cat_selected = ['food1', 'food2', 'food3', 'food4', 'food5'];
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

<form class = 'container mx-auto'>
    <div class="flex flex-wrap -mx-2">
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="Category" class="mb-2 text-xs">Category</Label>
            <Select id="select-category" style='font-size:x-small' size="sm" items={categories} placeholder="Category"/>
        </div>
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="Foodname" class="mb-2 text-xs" >Foodname</Label>
            <Input type="text" class='rounded' id="foodname" style='font-size:x-small' placeholder="Foodname" required/>
        </div>
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="Volume" class="mb-2 text-xs">Volume</Label>
            <Input type="number" class='rounded' id="volume" style='font-size:x-small' placeholder="Volume" required />
        </div>
    </div>
    <div class="flex flex-wrap -mx-2">
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="Unit" class="mb-2 text-xs">Unit</Label>
            <Select id="select-category" class='' size="md" style='font-size:x-small' items={units} placeholder="Unit"/>
        </div>
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="purchaseDate" class="mb-2 text-xs">Purchase Date</Label>
            <Input type="date" class=''  style='font-size:x-small' id="purchaseDate" required />
        </div>
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="expirationDate" class="mb-2 text-xs">Expiration date</Label>
            <Input type="date" class='' id="expirationDate" style='font-size:x-small' required />
        </div>
    </div>
    <Button type="submit" size = 'xs' style='font-size:x-small'>ADD</Button>
</form>

<div class="container mx-auto">
    <div class="flex flex-wrap -mx-2">
        {#each cat_selected as cat}
            <div class="w-1/3 p-2">
                <Card class="w-full">
                    <div class="flex-wrap text-xs">{cat}</div>
                </Card>
            </div>
        {/each}
    </div>
</div>


<Button type='submit' size = 'xs'> OK </Button>
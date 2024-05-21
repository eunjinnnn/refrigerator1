<script>
  import { Input, Label, Helper, Button, Checkbox, A , Select, Card} from 'flowbite-svelte';

  let lists = ['food1', 'food2', 'food3', 'food4', 'food5'];
  let cat_selected = ''
  let unit_selected = '';
  let volume = '';
  let foodname = '';
  let purchaseDate = '';
  let expirationDate = '';
  
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
    <div class = 'flex flex-wrap -mx-2 p-2'>
        <Label for="Category" class="mb-2 text-xs">Category</Label>
        <Select id="select-category"  bind:value={cat_selected} style='font-size:x-small' size="sm" items={categories} placeholder="Category"/>
    </div>
    <div class="flex flex-wrap -mx-2">
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="Foodname" class="mb-2 text-xs" >Foodname</Label>
            <Input type="text" bind:value={foodname} class='rounded' id="foodname" style='font-size:x-small' placeholder="Foodname" required/>
        </div>
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="Volume" class="mb-2 text-xs">Volume</Label>
            <Input type="number" bind:value = {volume} class='rounded' id="volume" style='font-size:x-small' placeholder="Volume" required />
        </div>
        <div class = 'flex flex-col w-1/3 p-2'>
            <Label for="Unit" class="mb-2 text-xs">Unit</Label>
            <Select id="select-category" bind:value = {unit_selected} class='' size="md" style='font-size:x-small' items={units} placeholder="Unit"/>
        </div>
    </div>
    <div class="flex flex-wrap -mx-2">
        <div class = 'flex flex-col w-1/2 p-2'>
            <Label for="purchaseDate" class="mb-2 text-xs">Purchase Date</Label>
            <Input type="date" bind:value = {purchaseDate} class=''  style='font-size:x-small' id="purchaseDate" required />
        </div>
        <div class = 'flex flex-col w-1/2 p-2'>
            <Label for="expirationDate" class="mb-2 text-xs">Expiration date</Label>
            <Input type="date" bind:value = {expirationDate} class='' id="expirationDate" style='font-size:x-small' required />
        </div>
    </div>
    <div class="flex justify-end">
        <Button type="submit" color = 'green' class="text-xs" style="font-size: x-small;">ADD</Button>
    </div>
</form>

<div class="container mx-auto">
    <div class="flex flex-wrap -mx-2">
        {#each lists as l}
            <div class="w-1/3 p-2">
                <Card class="w-full">
                    <div class="flex-wrap text-xs">{l}</div>
                </Card>
            </div>
        {/each}
    </div>
</div>

<p>{cat_selected || 'VEGETABLES'}</p>
<p>{foodname || 'food1'}</p>
<p>{volume ||'0'}</p>
<p>{unit_selected || '개'}</p>
<p>{purchaseDate || '2021-01-01'}</p>
<p>{expirationDate || '2021-01-01'}</p>


<div class="flex justify-end">
    <Button type='submit' color = 'green' size = 'xs'> OK </Button>
</div>
